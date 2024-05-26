from tabulate import tabulate

class ReportGenerator:
    @staticmethod
    def generate_poll_results(poll):
        if poll.poll_id is None:
            raise ValueError("Poll ID is not set.")

        # Fetch the options and their vote counts
        poll.db.cursor.execute("""
            SELECT OptionText, Votes 
            FROM PollOptions 
            WHERE PollID = ? 
            ORDER BY OptionID""", poll.poll_id)
        results = poll.db.cursor.fetchall()

        # Convert the results into a table
        headers = ["Option", "Votes"]
        table = tabulate(results, headers=headers, tablefmt="grid")

        return table
