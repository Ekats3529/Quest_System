import Quest


class QuestManager:
    statuses = ["disable", "active", "complete"]

    def __init__(self):
        pass

    @staticmethod
    def set_quest_status(self, quest, status):
        quest.change_status(status)

