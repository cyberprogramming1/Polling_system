# user.py

class User:
    def __init__(self, db):
        self.db = db

    def record_vote(self, poll_id, option_id, user_id):
        self.db.cursor.execute("INSERT INTO UserVotes (PollID, OptionID, UserID) VALUES (?, ?, ?)", (poll_id, option_id, user_id))
        self.db.commit()

    def get_votes_for_poll(self, poll_id):
        self.db.cursor.execute("""
            SELECT u.Username, po.OptionText
            FROM UserVotes uv
            JOIN Users u ON uv.UserID = u.UserID
            JOIN PollOptions po ON uv.OptionID = po.OptionID
            WHERE uv.PollID = ?
        """, (poll_id,))
        return self.db.cursor.fetchall()
