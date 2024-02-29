import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStream;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.List;

public class Day1 {
  private final List<List<Integer>> calories;

  public Day1() {
    calories = parseInput("input.txt");
  }

  int part1() {
    return calories.stream().
        mapToInt(elf -> elf.stream().mapToInt(Integer::intValue).sum()).
        max().getAsInt();
  }

  int part2() {
    List<Integer> summed = calories.stream().
        map(elf -> elf.stream().mapToInt(Integer::intValue).sum()).
        sorted().
        toList();

    int sum = 0;
    int lastIndex = summed.size() - 1;
    for (int i = lastIndex; i > lastIndex - 3; i--) {
      sum += summed.get(i);
    }

    return sum;
  }

  private static List<List<Integer>> parseInput(String file) {
    try {
      InputStream inputStream = Main.class.getResourceAsStream(file);
      BufferedReader reader = new BufferedReader(new InputStreamReader(inputStream));
      List<String> lines = reader.lines().toList();

      reader.close();
      inputStream.close();

      List<List<Integer>> calories = new ArrayList<>();
      List<Integer> elf = new ArrayList<>();
      for (String line : lines) {
        if (line.isEmpty()) {
          calories.add(elf);
          elf = new ArrayList<>();
        } else {
          elf.add(Integer.parseInt(line));
        }
      }

      if (!elf.isEmpty()) {
        calories.add(elf);
      }

      return calories;
    } catch (IOException e) {
      throw new RuntimeException(e);
    }
  }
}
