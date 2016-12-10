def writeBeDIT(vehicle, directory):
    f = open(directory, 'w')
    count = 1
    for i in vehicle:
        f.write('{:>4}'.format(str(i.head)))
        f.write('{:>2}'.format(str(i.date.date)))
        f.write('{:>2}'.format(str(i.date.month)))
        f.write('{:>2}'.format(str(i.date.year)))
        f.write('{:>2}'.format(str(i.time.hour)))
        f.write('{:>2}'.format(str(i.time.minute)))
        f.write('{:>2}'.format(str(i.time.second)))
        f.write('{:>2}'.format(str(int(i.time.second/60*100))))
        f.write('{:>3}'.format(str(int(round(i.speed)))))
        f.write('{:>4}'.format(str(int(round(i.gvm*10)))))
        f.write('{:>3}'.format(str(int(round(i.length*10)))))
        f.write('{:>2}'.format(str(int(round(i.axlen)))))
        f.write('{:>1}'.format(str(int(round(i.direction)))))
        f.write('{:>1}'.format(str(int(round(i.lane)))))
        f.write('{:>3}'.format(str(int(round(i.tlit)))))
        for j in range(0,19):
            f.write('{:>3}'.format(str(int(round(i.axlew[j]*10)))))
            f.write('{:>3}'.format(str(int(round(i.axles[j]*10)))))
        f.write('{:>3}'.format(str(int(round(i.axlew[19]*10)))))
        if count != len(vehicle):
            f.write('\n')
            count += 1
    f.close()
