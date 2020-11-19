

if __name__ == '__main__':
    f = open("./岗位详情2020-2")
    fw = open("./生成insert-sql", "w")
    counter = 34231
    for line in f.readlines():
        if counter == 0:
            counter = counter + 1
            continue
        gangs = line.split("---")
        gangs[-1] = gangs[-1].split("\n")[0]
        gangs.insert(0, counter)
        for i in range(0, len(gangs)):
            if type(gangs[i])==str and "本科" in gangs[i] and "研究生" in gangs[i-1]:
                a = gangs.pop(i)
                b = gangs.pop(i-1)
                gangs.insert(i - 1, "%s;%s" %(b, a))
                break

        fw.write("insert into jdwz_detail values %s;\n" % str(tuple(gangs)))
        counter = counter + 1
