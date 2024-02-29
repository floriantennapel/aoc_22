import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStream;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.List;

public class Main {
  private final List<int[]> strategy;

  public static void main(String[] args) {
    Main sol = new Main();
    System.out.println(sol.part1());
    System.out.println(sol.part2());
  }

  public Main() {
    strategy = parseInput("input.txt");
  }

  private int part1() {
    int sum = 0;

    for (int[] strat : strategy) {
      int result = rpsResult(strat[1], strat[0]);
      sum += result + strat[1];
    }

    return sum;
  }

  private int part2() {
    int sum = 0;

    for (int[] strat : strategy) {
      int choice = choiceGivenNeededResult(strat[0], strat[1]);
      choice += switch (strat[1]) {
        case 1 -> 0;
        case 2 -> 3;
        case 3 -> 6;
        default -> throw new IllegalArgumentException("result not possible");
      };
      sum += choice;
    }

    return sum;
  }

  private static List<int[]> parseInput(String file) {
    try {
      InputStream inputStream = Main.class.getResourceAsStream(file);
      BufferedReader reader = new BufferedReader(new InputStreamReader(inputStream));
      List<String> lines = reader.lines().toList();
      reader.close();
      inputStream.close();

      List<int[]> strategy = new ArrayList<>(lines.size());
      for (String line : lines) {
        int[] round = {
            rpsSymbolToValue(line.charAt(0)),
            rpsSymbolToValue(line.charAt(2))
        };
        strategy.add(round);
      }

      return strategy;
    } catch (IOException e) {
      throw new RuntimeException(e);
    }
  }

  private static int rpsSymbolToValue(char symbol) {
    return switch (symbol) {
      case 'A', 'X' -> 1;
      case 'B', 'Y' -> 2;
      case 'C', 'Z' -> 3;
      default -> throw new IllegalArgumentException("symbol not part of strategy");
    };
  }

  private static int rpsResult(int self, int opponent) {
    // 0 draw, 1 win, 2 loss
    int result = (self - opponent + 3) % 3;

    return switch (result) {
      case 2 -> 0;
      case 0 -> 3;
      default -> 6;
    };
  }

  private static int choiceGivenNeededResult(int opponent, int result) {
    int toAdd = switch (result) {
      case 1 -> -1;
      case 2 -> 0;
      case 3 -> 1;
      default -> throw new IllegalArgumentException("result not valid");
    };

    return (opponent + toAdd + 2) % 3 + 1;
  }
}
