import sys
import functools


def readingtext_file(path):
    with open(path) as f:
        lines = f.readlines()
    return lines

def extractonlytime(textdata):
    totallisttime=[]
    lines=textdata
    for i in lines:
        x=i.split()
        timeonly=[]
        for word in x:
            if not word.isalnum():
                if "/" not in word and "-" not in word:
                    timeonly.append(word)
        totallisttime.append(timeonly)
    return totallisttime


def filteronlytime(totallisttime):
    filtertime=[]
    for i in totallisttime:
        newlist=[]
        for k in i:
            if 'am' in k or 'pm' in k :
                    newlist.append(k)
        if len(newlist)!=0 and len(newlist)<=2:
            filtertime.append(newlist)
    return filtertime


def changingtimefarmat(filtertime):
    totallisttime=filtertime
    timediff={}
    for time in totallisttime:
        #print(time)
        timegplist=[]
        for t1 in  time:
            if 'pm' in t1.lower():
                chag_time=t1.split(':')
                timetochange=chag_time[0]
                if int(timetochange)!=12:

                    #print(int(changetime[0])+12)
                    chag_time.remove(timetochange)

                    chag_time.insert(0,str(int(timetochange)+12))
                    timegplist.append(int(':'.join(chag_time).replace('pm','').replace(':','')))
                else:
                    chag_time.remove(timetochange)

                    chag_time.insert(0,str(timetochange))
                    timegplist.append(int(':'.join(chag_time).replace('pm','').replace(':','')))
            else :
                #print(t1)
                if t1!='' :
                    chag_time=t1.split(':')
                    #print(changetime)
                    t=chag_time[0]
                    #print(t)
                    if int(t)!=12:
                    #print(int(changetime[0])+12)
                        chag_time.remove(t)

                        chag_time.insert(0,str(int(t)))
                        timegplist.append(int(':'.join(chag_time).replace('am','').replace(':','')))
                    else:
                        chag_time.remove(t)

                        chag_time.insert(0,str(24-int(0)))
                        timegplist.append(int(':'.join(chag_time).replace('am','').replace(':','')))
        #print(timegplist)

        timediff[''.join(time)]=timegplist
    return timediff


def counting_spent_time(timediff):
    import functools
    spent_time = {}
    for m1 in timediff.keys():
        # print(min)
        if m1 != None:
            x = timediff[m1]

            if len(x) > 0:

                yu = str(functools.reduce(lambda a, b: b - a, x))

                if len(yu) > 2:

                    spent_time[m1] = abs(int(yu[:-2]) * 60 + int(yu[-2:]))

                else:
                    spent_time[m1] = abs(int(yu))

            else:
                continue

    return spent_time


def main(filepath):
    read_text = readingtext_file(filepath)
    timedata = extractonlytime(read_text)
    onlytimedata = filteronlytime(timedata)
    stand_time = changingtimefarmat(onlytimedata)
    spent_total = counting_spent_time(stand_time)
    hours = str(round(sum(spent_total.values()) / 60, 2)).split('.')[0] + " hours"
    minutes = str(round(float("0." + str(round(sum(spent_total.values()) / 60, 2)).split('.')[-1]) * 60, 0)).split('.')[
                  0] + ' Min'
    spendtime = hours + ' ' + minutes
    time_1=filepath.lower().replace('timelog','').replace('.txt','')
    print(time_1.split('/')[-1])
    total_spent_time = 'time spent in ' +time_1.split('/')[-1]+' : ' +spendtime
    print(total_spent_time)
    return total_spent_time


if __name__ == "__main__":

    main(sys.argv[1])