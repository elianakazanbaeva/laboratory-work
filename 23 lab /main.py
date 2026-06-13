import TreeWork4
import TreeWork13
import TreeWork20


class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class ErrorHandler:
    @staticmethod
    def handle_input_error(error_msg):
        print(f"Ошибка ввода: {error_msg}")

    @staticmethod
    def handle_build_error(error_msg):
        print(f"Ошибка структуры: {error_msg}")

    @staticmethod
    def run_task_safely(module, class_name, method_name, root, label):
        try:
            task_class = getattr(module, class_name)
            method = getattr(task_class, method_name)
            result = method(root)

            if isinstance(result, list):
                if result:
                    formatted = ", ".join(str(item) for item in result)
                    print(f"{label}: {formatted}")
                else:
                    print(f"{label}: пусто")
            else:
                print(f"{label}: {result}")

        except AttributeError:
            print(f"{label}: Ошибка - класс или метод не найден в модуле.")
        except Exception as e:
            print(f"{label}: Ошибка выполнения - {e}")

class TreeController:
    def __init__(self):
        self.root = None
        self.error_handler = ErrorHandler()

    def load_data(self) -> bool:
        raw = input("Введите элементы дерева (через пробел, 'null' для пустых): ").strip()

        if not raw:
            self.error_handler.handle_input_error("пустой ввод")
            return False

        try:
            self.root = self._build_tree(raw.split())
            return True
        except ValueError as e:
            self.error_handler.handle_build_error(str(e))
            return False
        except Exception as e:
            self.error_handler.handle_build_error(f"неизвестная ошибка: {e}")
            return False

    def _build_tree(self, tokens: list) -> TreeNode:
        def parse(v):
            return None if v.lower() == 'null' else v

        if not tokens or parse(tokens[0]) is None:
            raise ValueError("Корень не может быть пустым.")

        root = TreeNode(parse(tokens[0]))
        queue = [root]
        idx = 1
        n = len(tokens)

        while queue and idx < n:
            node = queue.pop(0)

            if idx < n:
                val = parse(tokens[idx])
                if val is not None:
                    node.left = TreeNode(val)
                    queue.append(node.left)
                idx += 1

            if idx < n:
                val = parse(tokens[idx])
                if val is not None:
                    node.right = TreeNode(val)
                    queue.append(node.right)
                idx += 1

        return root

    def run_tasks(self):
        print("Результаты")

        tasks = [
            (TreeWork4, "TreeWork4", "get_leaves", "TreeWork4"),
            (TreeWork13, "TreeWork13", "count_leaves", "TreeWork13"),
            (TreeWork20, "AVLChecker", "is_balanced", "TreeWork20")
        ]

        for mod, cls_name, method, label in tasks:
            self.error_handler.run_task_safely(mod, cls_name, method, self.root, label)


if __name__ == "__main__":
    app = TreeController()
    if app.load_data():
        app.run_tasks()
