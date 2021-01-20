import argparse
import os

def artwork_parser(subparsers):
    artwork = subparsers.add_parser("artwork", help="download artworks from user ids specified in \"users\" field")
    artwork.add_argument("-a", metavar=("", "id"), type=int, nargs="+", help="add user ids")
    artwork.add_argument("-d", metavar=("all", "id"), nargs="+", help="delete user ids and their directories")
    artwork.add_argument("-c", metavar=("all", "id"), nargs="+", help="clear directories of user ids")

def bookmark_parser(subparsers):
    bookmark = subparsers.add_parser("bookmark" ,help="download bookmark artworks from user ids specified in \"bookmarks\" field")
    bookmark.add_argument("-a", metavar=("", "id"), type=int, nargs="+", help="add user ids")
    bookmark.add_argument("-d", metavar=("all", "id"), nargs="+", help="delete user ids and their directories")
    bookmark.add_argument("-c", metavar=("all", "id"), nargs="+", help="clear directories of user ids")

def ranking_parser(subparsers):
    modes = ["daily", "weekly", "monthly", "rookie", "original", "male", "female", "daily_r18", "weekly_r18", "male_r18", "female_r18"]
    contents = ["all", "illust", "ugoira", "manga"]
    ranking = subparsers.add_parser("ranking", help="download top N ranking artworks based on given conditions")
    ranking.add_argument("-m", metavar="MODE", choices=modes, required=True, help="modes: {%(choices)s}")
    ranking.add_argument("-c", metavar="CONTENT", choices=contents, required=True, help="contents: {%(choices)s}")
    ranking.add_argument("-d", metavar="YYYYMMDD", required=True, help="date ")
    ranking.add_argument("-n", metavar="N", type=int, default=20, help="get top N artworks (default: %(default)s)")

def main_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument("-f", metavar=("FILE"), default=os.path.join("data", "config.json"), help="load file for this instance (default: %(default)s)")
    parser.add_argument("-l", action="store_true", help="list current settings")
    parser.add_argument("-u", metavar=("USERNAME"), help="set username")
    parser.add_argument("-p", metavar=("PASSWORD"), help="set password")
    parser.add_argument("-s", metavar=("SAVE_DIR"), help="set save directory path")
    parser.add_argument("-t", metavar=("THREADS"), type=int, help="set number of threads for this instance")
    subparsers = parser.add_subparsers(dest="option")
    artwork_parser(subparsers)
    bookmark_parser(subparsers)
    ranking_parser(subparsers)
    return parser.parse_args()

