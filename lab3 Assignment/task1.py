from tgnpdcl_bill import calculate_bill, format_currency


def prompt_float(prompt_text: str):
	s = input(prompt_text).strip()
	if s == "":
		return None
	try:
		return float(s)
	except ValueError:
		print("Invalid number. Leaving blank to skip.")
		return None


def main():
	print("TGNPDCL - Energy Bill Generator\n")
	print("Enter previous and present meter readings (CU = previous, PU = present).")
	print("You may leave them blank and instead enter units directly.")
	cu = prompt_float("Enter Previous reading (CU): ")
	pu = prompt_float("Enter Present reading (PU): ")
	units = None
	if cu is not None and pu is not None:
		units = pu - cu
		if units < 0:
			print("Warning: Present reading less than previous reading. Taking absolute difference.")
			units = abs(units)
		print(f"Calculated units from readings: {units}")
	else:
		u = prompt_float("Enter units consumed directly (leave blank to use readings): ")
		if u is not None:
			units = u

	if units is None:
		print("No valid units provided. Exiting.")
		return

	print("\nCustomer types available: residential, commercial")
	ctype = input("Enter customer type: ").strip()
	try:
		bill = calculate_bill(units, ctype)
	except Exception as e:
		print(f"Error calculating bill: {e}")
		return

	print("\n--- Energy Bill ---")
	print(f"Energy Charges (EC):   {format_currency(bill['EC'])} INR")
	print(f"Fixed Charges (FC):    {format_currency(bill['FC'])} INR")
	print(f"Customer Charges (CC): {format_currency(bill['CC'])} INR")
	print(f"Electricity Duty (ED): {format_currency(bill['ED'])} INR")
	print("-------------------------------")
	print(f"Total Payable:         {format_currency(bill['Total'])} INR")


if _name_ == '_main_':
	main()
