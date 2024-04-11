def WhoAmI():
    return('sg4320')

def GetBondPrice(y,face,couponRate, m,ppy=1):
        # Calculate the coupon payment
    coupon_payment = face * couponRate / ppy
    # Initialize the bond price
    bondPrice = 0

    # Sum the present value of the coupons
    for t in range(1, m * ppy + 1):
        bondPrice += coupon_payment / ((1 + y / ppy) ** t)

    # Add the present value of the face value
    bondPrice += face / ((1 + y / ppy) ** (m * ppy))

    return bondPrice

def getBondDuration(y, face, couponRate, m, ppy=1):
    coupon_payment = face * couponRate / ppy
    bondDuration = 0
    bondPrice = 0

    # Calculate each cash flow's present value and weight by the time
    for t in range(1, m * ppy + 1):
        if t != m * ppy:
            # Coupon payment present value
            pv = coupon_payment / ((1 + y/ppy) ** t)
        else:
            # Final coupon payment plus face value present value
            pv = (coupon_payment + face) / ((1 + y/ppy) ** t)

        bondPrice += pv
        # Weight the pv by the time and add to duration
        bondDuration += t * pv

    # Divide by the bond's price to get the Macaulay duration
    bondDuration /= bondPrice

    return bondDuration

def getBondPrice_E(face, couponRate, yc):
    # Calculate the bond's maturity by the length of the yield curve
    m = len(yc)
    
    # Initialize the price of the bond
    bond_price = 0
    
    # Calculate the coupon payment
    coupon_payment = face * couponRate
    
    # Loop through each year up to maturity
    for t in range(1, m + 1):
        # Calculate the present value of the coupon payment
        # If it's the last year, add the face value to the coupon payment
        cash_flow = coupon_payment + (face if t == m else 0)
        # Discount the cash flow to present value using the yield for that year
        bond_price += cash_flow / ((1 + yc[t-1]) ** t)
    
    return bond_price

def getBondPrice_Z(face, couponRate, times, yc):
    # Calculate the coupon payment
    coupon_payment = face * couponRate
    
    # Initialize the bond price
    bondPrice = 0
    
    # Calculate the present value of each cash flow
    for t, y in zip(times, yc):
        if t != times[-1]:
            # Present value of coupon payments
            pv = coupon_payment / ((1 + y) ** t)
        else:
            # Present value of the final coupon payment plus face value
            pv = (coupon_payment + face) / ((1 + y) ** t)
        
        bondPrice += pv
    
    return bondPrice


def fizzbuzz(start, finish):
    outlist = []
    for i in range(start,finish+1):
        if i%3 == 0 and i%5 == 0:
            outlist.append('fizzbuzz')
        elif i%3 == 0:
            outlist.append('fizz')
        elif i%5 == 0:
            outlist.append('buzz')
        else:
            outlist.append(i)
    return outlist

