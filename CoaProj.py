class MonkeyBananaProblem:
    def __init__(self):
        self.state = ('door', 'floor', 'window', False)  # (monkey_pos, monkey_status, box_pos, has_banana)
        self.goal_state = ('middle', 'box', 'middle', True)  # Monkey on box under banana with banana

    def move(self, new_position):
        if self.state[3]:  # If monkey already has the banana, no need to move
            return "Monkey already has the banana!"
        if new_position in ("middle", "window", "door"):
            self.state = (new_position, self.state[1], self.state[2], self.state[3])
            return f"Monkey moved to {new_position}."
        return "Invalid move."

    def push_box(self, new_position):
        if self.state[0] == self.state[2] and new_position in ("middle", "window", "door"):
            self.state = (new_position, self.state[1], new_position, self.state[3])
            return f"Monkey pushed the box to {new_position}."
        return "Monkey must be at the box to push it."

    def climb_box(self):
        if self.state[0] == self.state[2]:  # Monkey can only climb if at the same position as the box
            self.state = (self.state[0], "box", self.state[2], self.state[3])  # Fix: Box position stays same
            return "Monkey climbed onto the box."
        return "Monkey must be at the box to climb it."

    def grasp_banana(self):
        if self.state[0] == "middle" and self.state[1] == "box" and self.state[2] == "middle" and not self.state[3]:  
            self.state = (self.state[0], self.state[1], self.state[2], True)
            return "Monkey grasped the banana!"
        return "Monkey must be on the box under the banana to grasp it."

    def solve(self):
        steps = []
        steps.append(self.move("window"))  # Move to box location
        steps.append(self.push_box("middle"))  # Push box to middle
        steps.append(self.move("middle"))  # Move to the middle (if needed)
        steps.append(self.climb_box())  # Climb box
        steps.append(self.grasp_banana())  # Grasp banana
        return steps


# Running the implementation
problem = MonkeyBananaProblem()
solution_steps = problem.solve()
for step in solution_steps:
    print(step)
