import numpy as np
from random import shuffle

def softmax_loss_naive(W, X, y, reg):
  """
  Softmax loss function, naive implementation (with loops)

  Inputs have dimension D, there are C classes, and we operate on minibatches
  of N examples.

  Inputs:
  - W: A numpy array of shape (D, C) containing weights.
  - X: A numpy array of shape (N, D) containing a minibatch of data.
  - y: A numpy array of shape (N,) containing training labels; y[i] = c means
    that X[i] has label c, where 0 <= c < C.
  - reg: (float) regularization strength

  Returns a tuple of:
  - loss as single float
  - gradient with respect to weights W; an array of same shape as W
  """
  # Initialize the loss and gradient to zero.
  loss = 0.0
  dW = np.zeros_like(W)
  num_train = X.shape[0]
  num_classes = W.shape[1]

  #############################################################################
  # TODO: Compute the softmax loss and its gradient using explicit loops.     #
  # Store the loss in loss and the gradient in dW. If you are not careful     #
  # here, it is easy to run into numeric instability. Don't forget the        #
  # regularization!                                                           #
  #############################################################################
  for i in range(num_train):
    score = np.dot(X[i], W)
    score -= score.max()
    score = np.exp(score)
    score = score/np.sum(score)
    for j in range(num_classes):
      if y[i] == j:
        loss += - 1 * np.log(score[j])
        dW[:, j] += - X[i] * (1 - score[j])
      else:
        dW[:, j] += X[i] * score[j]

  loss = loss/num_train + 0.5 * reg * np.sum(W * W)
  dW = 1/num_train * dW + reg * W

  #############################################################################
  #                          END OF YOUR CODE                                 #
  #############################################################################

  return loss, dW


def softmax_loss_vectorized(W, X, y, reg):
  """
  Softmax loss function, vectorized version.

  Inputs and outputs are the same as softmax_loss_naive.
  """
  # Initialize the loss and gradient to zero.
  loss = 0.0
  dW = np.zeros_like(W)
  num_train = X.shape[0]
  num_classes = W.shape[1]

  #############################################################################
  # TODO: Compute the softmax loss and its gradient using no explicit loops.  #
  # Store the loss in loss and the gradient in dW. If you are not careful     #
  # here, it is easy to run into numeric instability. Don't forget the        #
  # regularization!                                                           #
  #############################################################################
  class_true_score = np.zeros((num_train, num_classes))
  class_true_score[range(num_train), list(y)] = 1
  score = np.dot(X, W)
  score = score - score.max()
  score = np.exp(score)
  score = score / np.sum(score, axis = 1).reshape(-1,1)

  loss = (-1) * np.log(score) * class_true_score
  loss = 1/num_train * (np.sum(loss)) + 0.5 * reg * np.sum(W**2)

  s = score
  s[range(num_train), list(y)] = (-1) * (1 - score[range(num_train), list(y)])
  dW = 1/num_train * (np.dot(X.T, s)) + reg * W
  #############################################################################
  #                          END OF YOUR CODE                                 #
  #############################################################################

  return loss, dW

