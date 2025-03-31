def input_error(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError as e:
            return f"Error: {e}"
        except IndexError:
            return "Error: Missing required arguments."
        except KeyError:
            return "Error: Contact not found."
    return wrapper