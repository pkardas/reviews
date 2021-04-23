# reviews

Fetch reviews from TrustPilot.

## Usage

You can install this project using pip:

```shell
pip install git+https://github.com/pkardas/reviews.git
```

Saving to CSV:

```python
from reviews.trustpilot import get_reviews

get_reviews("https://www.trustpilot.com/review/github.com").to_csv()
get_reviews("https://www.trustpilot.com/review/github.com", limit=50).to_csv()
get_reviews("https://www.trustpilot.com/review/github.com", limit=50).to_csv("/pkardas/data")
```

Accessing reviews as Python objects:

```python
from reviews.trustpilot import get_reviews

trustpilot_reviews = get_reviews("https://www.trustpilot.com/review/github.com")
trustpilot_reviews.reviews
```

## Development

```bash
$ cd reviews
$ pyenv install 3.9.2
$ pyenv virtualenv 3.9.2 reviews
```

#### Configuring PyCharm to use the virtual environment
- Preferences (eg. MacOS: `⌘` + `,`)
- Project: `reviews` / Project interpreter
- Click on the "gear" icon, and then select "Add"
- Virtualenv environment
- Existing environment
- Choose Python 3.9.2 (reviews) that should me located in `~/.pyenv/versions/reviews/bin/python3`

