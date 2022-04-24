"""Script defining the route to serve commands."""

from flask import Blueprint, flash, jsonify, request

from flaskr.db import get_db

cmd_route = Blueprint("cmd_route", __name__)

@cmd_route.route('/commands', methods=(['GET']))
def get_cmds():
    """Get route for retreiving all the commands in the app."""
    # Get the db
    db = get_db()
    
    # Try to get all commands
    try:
        cmds = db.execute("SELECT * FROM commands")
        results = cmds.fetchall()
        commands = []
        for row in results:
            row_as_dict = {cmds.description[i][0]:row[i] for i in range(len(row))}
            commands.append(row_as_dict)
    except db.IntegrityError:
        error = f"Integrity error"
        flash(error)
    
    return jsonify(commands)

@cmd_route.route('/post-command', methods=(['POST']))
def post_cmd():
    """Post command to add a new command to the database."""
    command = request.form['command']
    description = request.form['description']
    example = request.form['example']
    cli = request.form['cli']
    
    db = get_db()
    error = None
    
    if command is None:
        error = 'Command required'
    if cli is None:
        error = 'CLI is required'
    
    if error is None:
        try:
            db.execute(
                "INSERT INTO commands (command, description, example, cli) VALUES (?, ?, ?, ?)",
                (command, description, example, cli),
            )
            db.commit()
        except db.IntegrityError:
            error = f"Command {command} is already registered."
        
            flash(error)
    
    return "201"