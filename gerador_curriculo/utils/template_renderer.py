import jinja2

def create_latex_environment():
    # Set up Jinja2 environment with custom delimiters for LaTeX
    env = jinja2.Environment(
        block_start_string="((*",         # Start block statements
        block_end_string="*))",           # End block statements
        variable_start_string="(((",      # Start expressions/variables
        variable_end_string=")))",       # End expressions/variables
        comment_start_string="((=",       # Start comments
        comment_end_string="=))",        # End comments
    )
    return env
