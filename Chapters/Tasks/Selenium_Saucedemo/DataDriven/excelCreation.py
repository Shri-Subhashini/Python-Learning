from openpyxl import Workbook

workbook = Workbook()
sheet = workbook.active
sheet.title = "LoginData"

# Add headers
sheet.append(["Username", "Password"])

# Add some test data
sheet.append(["standard_user", "secret_sauce"])
sheet.append(["locked_out_user", "secret_sauce"])
# sheet.append(["performance_glitch_user", "secret_sauce"])


# Save the file
workbook.save("testData.xlsx")
