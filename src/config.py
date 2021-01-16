class configuration:

    def __init__(self):

        # Network Setup
        # True = I am using the polipo Proxy on a Linux Host
        # False = I am using Tails or Whonix
        self.use_proxy = False

        # Database Setup:
        self.db_name = "onion.db"
        self.save_html_source_to_db = False

        # Reddit API Variables
        self.r_username = ""
        self.r_password = ""
        self.r_client_id = ""
        self.r_client_secret = ""
        self.r_user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:71.0) Gecko/20100101 Firefox/71.0"

        # AWS Credentials
        self.aws_access_key = ""
        self.aws_secret_key = ""

        # Reddit SubReddits to Search:
        self.sub_reddits = [
            "onions",
            "deepweb",
            "darknet",
            "tor",
            "conspiracy",
            "privacy",
            "vpn",
            "deepwebintel",
            "emailprivacy",
            "drugs",
            "blackhat",
            "HowToHack",
            "netsec",
            "hacking",
            "blackhatunderground",
            "blackhats",
            "blackhatting",
            "blackhatexploits",
            "reverseengineering",
        ]

        self.keywords = ["Add", "Keywords", "here"]
