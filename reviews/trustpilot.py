import csv
from typing import List, Optional

from bs4 import BeautifulSoup

from reviews.gateways import get_website_html
from reviews.models import Review


class TrustPilotReviews:
    def __init__(self, reviews: List[Review]) -> None:
        self.reviews = reviews

    def to_csv(self, folder_path: str = ".") -> None:
        with open(f"{folder_path}/reviews.csv", mode='w') as csv_file:
            writer = csv.DictWriter(csv_file, fieldnames=["header", "content", "rating"])

            writer.writeheader()
            for review in self.reviews:
                writer.writerow(review.to_dict())


def get_reviews(url: str, limit: int = 50) -> TrustPilotReviews:
    reviews = []

    while len(reviews) < limit:
        page_source = get_website_html(url)

        if not page_source:
            break

        soup = BeautifulSoup(page_source, "html.parser")

        if new_reviews := _get_visible_reviews(soup):
            reviews += new_reviews
            print(f"Downloaded {len(new_reviews)} reviews ({len(reviews)} in total).")
        else:
            print(f"No more reviews available.")
            break

        url = _next_subpage(soup)

        if not url:
            print("Could not find next subpage.")
            break

    return TrustPilotReviews(reviews[:limit])


def _get_visible_reviews(soup: BeautifulSoup) -> List[Review]:
    """
    Downloads approx. 20 reviews from a single subpage.
    """
    review_cards = soup.findAll("div", {"class": "review-card"})

    reviews = []
    for review_card in review_cards:
        header = review_card.findAll("a", {"class": "link link--large link--dark"})[0].get_text().strip()

        body = review_card.findAll("p", {"class": "review-content__text"})
        content = body[0].get_text().strip() if body else None

        rating = review_card.findAll("div", {"class": "star-rating star-rating--medium"})[0].img["alt"].strip()

        reviews.append(Review(header, content, rating))

    return reviews


def _next_subpage(soup: BeautifulSoup) -> Optional[str]:
    """
    TrustPilot no longer uses consecutive natural numbers as subpage URLs.
    This function finds "Next page" button and extracts 'href' attribute.
    """
    buttons = soup.findAll("a", {"class": "button button--primary next-page"})

    if not buttons:
        return None

    return f"https://www.trustpilot.com{buttons[0]['href']}"
