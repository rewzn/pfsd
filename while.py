def countdown(n):
    while n > 0:
        print n
        n = n - 1
    print 'Blastoff!'

countdown(int(raw_input('Zahl eingeben: ')))
