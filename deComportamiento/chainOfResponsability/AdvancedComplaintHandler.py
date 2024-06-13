from ComplaintHandler import ComplaintHandler
class AdvancedComplaintHandler(ComplaintHandler):
    def handle_complaint(self, complaint):
        if complaint == "major":
            print("Advanced handler resolves the major issue.")
        else:
            super().handle_complaint(complaint)