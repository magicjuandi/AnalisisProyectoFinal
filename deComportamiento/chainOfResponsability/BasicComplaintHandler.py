from ComplaintHandler import ComplaintHandler
class BasicComplaintHandler(ComplaintHandler):
    def handle_complaint(self, complaint):
        if complaint == "minor":
            print("Basic handler resolves the minor issue.")
        else:
            super().handle_complaint(complaint)