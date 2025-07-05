def player(prev_play, opponent_history=[], play_order=[{}]):
    # Update history
    if prev_play != "":
        opponent_history.append(prev_play)

    # Default first move
    if len(opponent_history) < 2:
        return "R"

    # Update play_order map for sequence prediction
    last_two = "".join(opponent_history[-2:])
    if last_two not in play_order[0]:
        play_order[0][last_two] = 0
    play_order[0][last_two] += 1

    # Predict next opponent move using last opponent move
    last = opponent_history[-1]
    options = [last + "R", last + "P", last + "S"]
    predictions = {k: play_order[0].get(k, 0) for k in options}
    prediction = max(predictions, key=predictions.get)[-1]

    # Counter the predicted move
    counter = {'R': 'P', 'P': 'S', 'S': 'R'}
    return counter[prediction]
