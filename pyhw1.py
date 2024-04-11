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

def getBondPrice_E(face, couponRate, m, yc):
    coupon_payment = face * couponRate
    bondPrice = 0

    # Loop over each time period and corresponding yield curve rate
    for t, y in enumerate(yc, start=1):
        if t != m:
            # Present value of coupon payments
            pv = coupon_payment / ((1 + y) ** t)
        else:
            # Present value of the final coupon payment plus face value
            pv = (coupon_payment + face) / ((1 + y) ** t)
        
        bondPrice += pv

    return bondPrice

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

