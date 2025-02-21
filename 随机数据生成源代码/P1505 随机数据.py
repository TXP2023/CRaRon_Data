from cyaron import * # 引入CYaRon的库

#output_path = "D:\bobi2\development\work spaces\OI-code\input.txt"
#output_path = "test1.out"

io = IO("test1.in", "..\\test1.out") # 先新建一组数据
#io = IO("test1.in", "D:\bobi2\development\work spaces\OI-code\input.txt") # 先新建一组数据

_n = ati([0, 7, 50, 1E4]) # ati函数将数组中的每一个元素转换为整形，方便您可以使用1E4一类的数来表示数据大小
_m = ati([0, 11, 100, 1E4]) 

n = randint(4, 6)

io.input_writeln(n)

graph = Graph.graph(n, n - 1, weight_limit=20) # 生成一个n点，m边的无向图，边权范围是1到20
io.input_writeln(graph)

str = ['C','N','SUM','MAX','MIN']

m = randint(3, 8)

io.input_writeln(m);

for i in range(m):
    s = str[randint(0, 4)]
    io.input_write(s)
    if s == 'C':
        io.input_writeln(randint(0, n - 1), randint(0, 20))
    else :
        #io.input_writeln(randint(0, 4), randint(0, 4))
        u = randint(0, n - 1)
        v = u
        while u == v:
            v = randint(0, n - 1)
        io.input_writeln(u, v)

    
        

