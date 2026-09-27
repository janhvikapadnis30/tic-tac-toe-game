export class Board {
  constructor() {
    this.grid = Array(9).fill("");
  }

  reset() {
    this.grid = Array(9).fill("");
  }

  updateCell(index, mark) {
    if (this.grid[index] === "") {
      this.grid[index] = mark;
      return true;
    }
    return false;
  }

  getGrid() {
    return this.grid;
  }
}
