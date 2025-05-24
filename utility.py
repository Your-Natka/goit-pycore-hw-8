def input_error(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except IndexError:
            return "Missing required arguments."
        except ValueError:
            return "Invalid argument value."
        except KeyError:
            return "Contact not found."
        except Exception as e:
            return f"Error: {e}"
    return wrapper
