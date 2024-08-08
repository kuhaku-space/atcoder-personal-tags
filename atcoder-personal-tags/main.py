from .services.migration import Migration
from .services.tag import create_tag_data


def main():
    Migration().create()
    create_tag_data()


if __name__ == "__main__":
    main()
