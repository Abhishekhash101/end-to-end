import sys
import logging

def error_message_detail(error, erro_detail:sys):
    _,_,exe_tb=erro_detail.exc_info()
    file_name=exe_tb.tb_frame.f_code.co_filename
    error_message=f"Error Occured in python Script name {file_name} in the line number {exe_tb.tb_lineno} error message {error}"

    return error_message

class CustomException(Exception):
    def __init__(self, error_message, error_detail:sys):
        super().__init__(error_message)
        self.error_message=error_message_detail(error_message,erro_detail=error_detail)


if __name__=="__main__":
    try:
        a=1/0
    except Exception as e:
        
        raise CustomException(e,sys)


