from Robot import Robot

def get_sample_input():
    return '''########
    #..O.O.#
    ##@.O..#
    #...O..#
    #.#.O..#
    #...O..#
    #......#
    ########

    <^^>>>vv<v>>v<<'''


def convert_to_graph_and_guidepath(input_str):  
    top, bottom = input_str.strip().split('\n\n')
    matrix_str = top.split("\n")
    guidepath_str = bottom.split("\n")
    graph = [list(row.strip()) for row in matrix_str]
    guidepath = [list(row.strip()) for row in guidepath_str]
    
    return graph, guidepath


graph, guidepath = convert_to_graph_and_guidepath(get_sample_input())


robot = Robot(graph)

for path in guidepath:
    for direction in path:  # Each path can have multiple directions
        print(f"\nMoving {direction}:")
        if robot.move(direction):
            robot.print_grid()
        else:
            print("Move failed.")
