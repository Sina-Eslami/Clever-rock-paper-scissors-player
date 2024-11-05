FreeCodeCamp Machine Learning Project: AI Opponent Strategy
This repository contains my first project from the FreeCodeCamp Machine Learning course: developing an AI that can outperform various algorithms in a competitive game environment.

Project Overview
The goal of this project was to create a function (def) that can consistently win over 50% of games against different algorithmic opponents.
I explored multiple machine learning approaches, including Q-learning and neural networks, to develop and test various strategies.

Methodology
Throughout this project, I experimented with several approaches:

Q-learning and Reinforcement Learning:
Initial tests involved Q-learning, but while the results were promising, they fell short of the target 60% win rate.
Pattern Recognition with Play History:
In the final version, I implemented a pattern-based method. This approach saves the opponent's previous moves in a Python list and identifies recurring patterns (sequences of 2, 3, 4, or 5 moves).
Using these patterns, the model predicts the opponent's next move, improving win rates significantly.

Results
After fine-tuning the model, this pattern-recognition approach achieved the highest win rate. Although the model reached above 50% wins after 1000 rounds,
the ultimate goal was to achieve a win rate exceeding 60%, which this method came closest to fulfilling.

Conclusion
This project was a great introduction to machine learning techniques in game strategy,
helping me understand the strengths and limitations of various algorithms. While the pattern-based approach proved to be the most effective,
there are still opportunities for further optimization and exploration in predictive modeling.
