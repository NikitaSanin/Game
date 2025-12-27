from entity import Entity
import collections

class BaseEnemy(Entity):
    def __init__(self, x, y, hp, max_ap, name, damage, color, scale):
        super().__init__(x, y, hp, max_ap, name)
        self.damage = damage
        self.color = color
        self.scale = scale
        self.active_effects = []

    def add_effect(self, effect):
        self.active_effects.append(effect)

        self.log(f"{self.name} отримав ефект '{effect.name}'!")

    def ai_move(self, target_entity, game_map, all_enemies):

        if self.hp <= 0: return

        self.ap = self.max_ap
        for effect in self.active_effects:
            self.ap = effect.modify_ap(self.ap)

        if self.ap < self.max_ap:
            self.log(f"{self.name} має лише {self.ap} АП через ефекти.")

        while self.ap > 0:
            dist = abs(self.x - target_entity.x) + abs(self.y - target_entity.y)

            if dist <= 1:
                cost_attack = 1
                if self.ap >= cost_attack:
                    target_entity.hp -= self.damage
                    self.ap -= cost_attack
                    self.log(f"{self.name} атакував на {self.damage} урону!")
                else:
                    break

            else:
                cost_move = 1
                if self.ap >= cost_move:
                    next_step = self.find_path_bfs(target_entity, game_map, all_enemies)

                    if next_step:
                        nx, ny = next_step
                        self.x = nx
                        self.y = ny
                        self.ap -= cost_move
                    else:
                        break
                else:
                    break

        self.active_effects = [e for e in self.active_effects if e.on_turn_end()]

    def find_path_bfs(self, target, game_map, all_enemies):

        start = (self.x, self.y)
        goal = (target.x, target.y)

        queue = collections.deque([(start, [])])

        visited = set()
        visited.add(start)

        enemy_positions = {(e.x, e.y) for e in all_enemies if e != self and e.hp > 0}

        while queue:
            (curr_x, curr_y), path = queue.popleft()

            if (curr_x, curr_y) == goal:
                if path:
                    return path[0]
                return None

            for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                nx, ny = curr_x + dx, curr_y + dy

                if 0 <= ny < len(game_map) and 0 <= nx < len(game_map[0]):
                    if game_map[ny][nx] == 1:
                        continue

                    if (nx, ny) in enemy_positions and (nx, ny) != goal:
                        continue

                    if (nx, ny) not in visited:
                        visited.add((nx, ny))
                        new_path = path + [(nx, ny)]
                        queue.append(((nx, ny), new_path))
        return None