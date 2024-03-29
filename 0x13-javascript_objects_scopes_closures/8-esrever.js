#!/usr/bin/node
exports.esrever = function (list) {
  const _list = [...list];
  const N = _list.length; const lrnHalf = parseInt(N / 2); let i;
  for (i = 0; i < lrnHalf; i++) {
    const tmp = _list[i];
    _list[i] = _list[N - 1 - i];
    _list[N - 1 - i] = tmp;
  }
  return _list;
};
