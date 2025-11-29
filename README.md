# car-poor
The Car Poor tool is a personal finance tool intended to help people avoid being car poor.
The tool combines well established best practice recommendations for car buying and allows comparison of multiple potential car buying options.

**Goal**:
1. Establish how much car you can actually afford based off of your annual income
2. Determine your current cars value and oportunity cost loss based on fuel economy and repairs
3. Determine the actual out the door price of a car make and model you are considering
3. Compair several potential car buying scenarios and export as a CSV file

**How to use:**


**Technical/Design:**
*Variables in:*
- yearly_income: given as XX,XXX 
- enthusiast_level: low = 25% , medium = 30% , high = 35%
- current_car_val: given as XX,XXX
- future_car_val: given as XX,XXX
- loan_term: given in months
- APR: given as a percentage eg; 5%, Defaults to a pulled national average rounded up one decimal place
- State_residence: Given as 2 character string eg; XX
*Variables out:*
- 
*Guidelines:*
- User should be able to modify yearly income, enthusiast level, current car value, future car value, down payment, loan term, APR, and State of residence
- User should then be able to export any given scenario as a CSV file for later analysis
- Program should default to a "idealistic" mode that gives the ideal scenario based soley on income


