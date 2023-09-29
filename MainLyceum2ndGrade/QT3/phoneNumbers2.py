def to_std(tel):
    _error_msg = "error"
    try:
        tel = "".join(tel.split())

        if tel.find("+7") != 0 and tel.find("8") != 0:
            raise ValueError("Неверный формат номера")
        
        if not all(tel.split("-")):
            raise ValueError("Неверный формат номера")
        else:
            tel = tel.replace("-", "")

        start_bt = tel.find("(")
        end_bt = tel.find(")")

        if start_bt > -1:
            if end_bt < start_bt or not tel[start_bt + 1:end_bt].isdigit() \
                    or not tel.count("(") == 1 or not tel.count(")") == 1:
                raise ValueError("Неверный формат номера")
            
        else:
            if end_bt > -1:
                raise ValueError("Неверный формат номера")
            
        tel = tel.replace("(", "")
        tel = tel.replace(")", "")

        if tel.find("8") == 0:
            tel = "+7" + tel[1:]

        if not tel[1:].isdigit() or not len(tel[1:]) == 11:
            raise ValueError("Неверный формат номера")
        
        return tel
    except (ValueError, TypeError):
        return _error_msg
    except Exception:
        return _error_msg


if __name__ == "__main__":
    print(to_std(input()))