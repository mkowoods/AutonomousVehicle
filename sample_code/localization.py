colors = [['red', 'green', 'green',   'red', 'red'],
          ['red',   'red', 'green',   'red', 'red'],
          ['red',   'red', 'green', 'green', 'red'],
          ['red',   'red',   'red',   'red', 'red']]

measurements = ['green', 'green', 'green' ,'green', 'green']

p = [[1./20, 1./20, 1./20, 1./20, 1./20],
     [1./20, 1./20, 1./20, 1./20, 1./20],
     [1./20, 1./20, 1./20, 1./20, 1./20],
     [1./20, 1./20, 1./20, 1./20, 1./20]]

motions = [[0,0],[0,1],[1,0],[1,0],[0,1]]

sensor_right = 0.7

p_move = 0.8

def show(p):
    for i in range(len(p)):
        print p[i]

#Do not delete this comment!
#Do not use any import statements.
#Adding or changing any code above may
#cause the assignment to be graded incorrectly.

#Enter your code here:
def shape(arr):
    return len(arr), len(arr[0])

def sum_array(arr):
    total = 0.0
    for row in arr:
        for cell in row:
            total += cell
    return total

def copy_arr(arr):
    tmp_arr = []
    for row in arr:
        tmp_row = []
        for cell in row:
            tmp_row.append(cell)
        tmp_arr.append(tmp_row)
    return tmp_arr

def zeroes(arr):
    tmp_arr = []
    for row in arr:
        tmp_row = []
        for cell in row:
            tmp_row.append(0)
        tmp_arr.append(tmp_row)
    return tmp_arr

def normalize_arr(arr):
    q = copy_arr(arr)
    total = sum_array(arr)
    rows, cols = shape(p)
    for i in range(rows):
        for j in range(cols):
            q[i][j] = arr[i][j]/total
    return q

def sense(p, meas, sensor_accuracy):
    q = copy_arr(p)
    rows, cols = shape(p)
    for i in range(rows):
        for j in range(cols):
            if colors[i][j] == meas:
                q[i][j] = p[i][j]*sensor_accuracy
            else:
                q[i][j] = p[i][j]*(1 - sensor_accuracy)
    return normalize_arr(q)

def move(p, move, move_acc):
    q = zeroes(p)
    rows, cols = shape(p)
    for i in range(rows):
        for j in range(cols):
            q[i][j] += p[i][j] * (1 - move_acc)
            q[(i+move[0])%rows][(j+move[1])%cols] += p[i][j]*move_acc

    return normalize_arr(q)






for i in range(len(motions)):
    p = move(p, motions[i], p_move)
    #show(p)
    p = sense(p, measurements[i], sensor_right)
    #show(p)




#Your probability array must be printed 
#with the following code.

show(p)


# test 1
colors = [['G', 'G', 'G'],
          ['G', 'R', 'G'],
          ['G', 'G', 'G']]
measurements = ['R']
motions = [[0,0]]
sensor_right = 1.0
p_move = 1.0
p = localize(colors,measurements,motions,sensor_right,p_move)
correct_answer = (
    [[0.0, 0.0, 0.0],
     [0.0, 1.0, 0.0],
     [0.0, 0.0, 0.0]])

# test 2
colors = [['G', 'G', 'G'],
          ['G', 'R', 'R'],
          ['G', 'G', 'G']]
measurements = ['R']
motions = [[0,0]]
sensor_right = 1.0
p_move = 1.0
p = localize(colors,measurements,motions,sensor_right,p_move)
correct_answer = (
    [[0.0, 0.0, 0.0],
     [0.0, 0.5, 0.5],
     [0.0, 0.0, 0.0]])

# test 3
colors = [['G', 'G', 'G'],
          ['G', 'R', 'R'],
          ['G', 'G', 'G']]
measurements = ['R']
motions = [[0,0]]
sensor_right = 0.8
p_move = 1.0
p = localize(colors,measurements,motions,sensor_right,p_move)
correct_answer = (
    [[0.06666666666, 0.06666666666, 0.06666666666],
     [0.06666666666, 0.26666666666, 0.26666666666],
     [0.06666666666, 0.06666666666, 0.06666666666]])

# test 4
colors = [['G', 'G', 'G'],
          ['G', 'R', 'R'],
          ['G', 'G', 'G']]
measurements = ['R', 'R']
motions = [[0,0], [0,1]]
sensor_right = 0.8
p_move = 1.0
p = localize(colors,measurements,motions,sensor_right,p_move)
correct_answer = (
    [[0.03333333333, 0.03333333333, 0.03333333333],
     [0.13333333333, 0.13333333333, 0.53333333333],
     [0.03333333333, 0.03333333333, 0.03333333333]])

# test 5
colors = [['G', 'G', 'G'],
          ['G', 'R', 'R'],
          ['G', 'G', 'G']]
measurements = ['R', 'R']
motions = [[0,0], [0,1]]
sensor_right = 1.0
p_move = 1.0
p = localize(colors,measurements,motions,sensor_right,p_move)
correct_answer = (
    [[0.0, 0.0, 0.0],
     [0.0, 0.0, 1.0],
     [0.0, 0.0, 0.0]])

# test 6
colors = [['G', 'G', 'G'],
          ['G', 'R', 'R'],
          ['G', 'G', 'G']]
measurements = ['R', 'R']
motions = [[0,0], [0,1]]
sensor_right = 0.8
p_move = 0.5
p = localize(colors,measurements,motions,sensor_right,p_move)
correct_answer = (
    [[0.0289855072, 0.0289855072, 0.0289855072],
     [0.0724637681, 0.2898550724, 0.4637681159],
     [0.0289855072, 0.0289855072, 0.0289855072]])

# test 7
colors = [['G', 'G', 'G'],
          ['G', 'R', 'R'],
          ['G', 'G', 'G']]
measurements = ['R', 'R']
motions = [[0,0], [0,1]]
sensor_right = 1.0
p_move = 0.5
p = localize(colors,measurements,motions,sensor_right,p_move)
correct_answer = (
    [[0.0, 0.0, 0.0],
     [0.0, 0.33333333, 0.66666666],
     [0.0, 0.0, 0.0]])