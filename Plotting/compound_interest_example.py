import pylab as plt

def retire(monthly, rate, terms):
    savings = [0]
    base = [0]
    mRate = rate / 12

    for i in range(terms):
        # Build 2 lists that represent x and y axes.
        base += [i]
        savings += [savings[-1]*(1+mRate)+monthly]

    return base, savings

def displayRetireWMonthlies(monthlies, rate, terms):
    plt.figure('retireMonth')
    plt.clf()
    for monthly in monthlies:
        xvals, yvals = retire(monthly, rate, terms)
        # Put monthly label.
        plt.plot(xvals, yvals, label = 'retire: '+str(monthly))
        plt.legend(loc = 'upper left')
    # Avoid scales being shown using scientific exponential notation.
    plt.ticklabel_format(style='plain')
    plt.show()

def displayRetireWRates(month, rates, terms):
    plt.figure('retireRate')
    plt.clf()
    for rate in rates:
        xvals, yvals = retire(month, rate, terms)
        plt.plot(xvals, yvals,
                 label = 'retire: '+str(month)+ ':' + \
                         str(int(rate*100)))
        plt.legend(loc = 'upper left')
    # Avoid scales being shown using scientific exponential notation.
    plt.ticklabel_format(style='plain')
    plt.show()

def displayRetireWRatesAndMonths(monthlies, rates, terms):
    plt.figure('retireBoth')
    plt.clf()
    plt.xlim(30*12,40*12) # Only look at last 10 years.
    # Create sets of labels.
    monthLabels = ['r','b','g','k']
    rateLabels = ['-','^','--']
    for i in range(len(monthlies)):
        monthly = monthlies[i]
        # Pick new label for each month choice.
        monthLabel = monthLabels[i % len(monthLabels)]
        for j in range(len(rateLabels)):
            rate = rates[j]
            rateLabel = rateLabels[j % len(rateLabels)]
            xvals, yvals = retire(monthly, rate, terms)
            plt.plot(xvals, yvals, monthLabel+rateLabel,
                     label = 'retire: '+str(monthly)+ ':' + \
                             str(int(rate*100)))
            plt.legend(loc = 'upper left')
    # Avoid scales being shown using scientific exponential notation.
    plt.ticklabel_format(style='plain')
    plt.show()

# displayRetireWMonthlies([500,600,700,800,900,1000,1100,1200],0.05,40*12)
# displayRetireWRates(800,[0.03,0.05,0.07],40*12)
displayRetireWRatesAndMonths([500,700,900,1100],[0.03,0.05,0.07],40*12)
