from BasicComplaintHandler import BasicComplaintHandler
from AdvancedComplaintHandler import AdvancedComplaintHandler
from UltimateComplaintHandler import UltimateComplaintHandler
if __name__ == "__main__":
    ultimate_handler = UltimateComplaintHandler()
    advanced_handler = AdvancedComplaintHandler(ultimate_handler)
    basic_handler = BasicComplaintHandler(advanced_handler)

    complaint = "major"
    basic_handler.handle_complaint(complaint)