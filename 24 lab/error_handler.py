class ErrorHandler:
    @staticmethod
    def parse_dll_input(raw):
        try:
            if not raw or not raw.strip():
                return []
            values = [int(x) for x in raw.split()]
            if values != sorted(values):
                values.sort()
            return values
        except ValueError:
            raise ValueError('Список должен содержать только целые числа.')

    @staticmethod
    def parse_tree_input(raw):
        try:
            if not raw or not raw.strip():
                return []
            parts = raw.split()
            result = []
            for p in parts:
                if p.lower() in ('none', 'null', '#'):
                    result.append(None)
                else:
                    result.append(int(p))
            return result
        except ValueError:
            raise ValueError('Дерево должно содержать числа или None.')

    @staticmethod
    def safe_execute(task_name, func, *args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            print(f'Ошибка в {task_name}: {e}')
            return None