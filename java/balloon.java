package comp_251_a5;
import java.io.*;
import java.util.*;


public class balloon {
	private int tests;
	private int[] balloon_numbers;
	ArrayList<int[]> heights = new ArrayList<int[]>();
	balloon(){
		try {
	        Scanner f = new Scanner(new File("testBalloons.txt"));
	        String[] ln = f.nextLine().split("\\s+"); 
	        this.tests = Integer.parseInt(ln[0]);
	        int test_number = 0;
	        balloon_numbers = new int[this.tests];
	        String[] line = f.nextLine().split("\\s+");
	        for(int i = 0;i<tests;i++) {
	        	balloon_numbers[i] = Integer.parseInt(line[i]);
	        }
	        for(int i = 0;i<tests;i++) {
	        	int[] current_heights = new int[balloon_numbers[i]];
	        	line = f.nextLine().split("\\s+");
	        	for(int j = 0 ;j<balloon_numbers[i];j++){
	        		current_heights[j] = Integer.parseInt(line[j]);
	        	}
	        	
	        	heights.add(current_heights);
	            
	        }
	        f.close();
	     
	    }
	    catch (FileNotFoundException e){
	        System.out.println("File not found!");
	        System.exit(1);
	    }
	}
	public int pew(int[] heights,int balloons){
		int[] remaining_balloons = heights.clone();
		int arrows = 0;
		int current_arrow_height = 0;
		int new_remaining = 0;
		int balloons_left = remaining_balloons.length;
		ArrayList<ArrayList<Integer>> trajectories = new ArrayList<ArrayList<Integer>>();
		ArrayList<Integer> current_trajectory = new ArrayList<Integer>();
		while(balloons_left>0){
			int[] max_height = FindMax(remaining_balloons);
			
			current_arrow_height = max_height[1];
			current_trajectory.add(current_arrow_height);
			balloons_left--;
			remaining_balloons[max_height[0]] = 0;
			for(int i = max_height[0];i<remaining_balloons.length;i++){
				if(current_arrow_height==1){
					break;
				}
				if(remaining_balloons[i]==current_arrow_height-1&&remaining_balloons[i]!= 0){
					
					current_arrow_height--;
					current_trajectory.add(current_arrow_height);
					remaining_balloons[i] = 0;
					balloons_left--;
					
				}
			}
			trajectories.add(current_trajectory);
			current_trajectory.clear();
			new_remaining = 0;
			
		}
		arrows = trajectories.size();
		return arrows;
	}
	public int[] FindMax(int[] heights){
		int[] max_height = new int[2];
		max_height[0] = 0; max_height[1] = 0;
		for(int i = 0;i<heights.length;i++){
			if(heights[i]>max_height[1]){
				max_height = (new int[] {i,heights[i]});
			}
		}
		return max_height;
	}
	public int[] GetHeights(int index) {
		return this.heights.get(index);
	}
	public int GetBalloonNum(int index) {
		return this.balloon_numbers[index];
	}
	public int GetTests() {
		return this.tests;
	}
	public static void writeAnswer(int line) {
		BufferedReader br = null;
		File file = new File("testBalloons_solution.txt");
		// if file doesnt exists, then create it

		try {
			if (!file.exists()) {
				file.createNewFile();
			}
			FileWriter fw = new FileWriter(file, true);
			BufferedWriter bw = new BufferedWriter(fw);
			bw.write(line + "\n");
			bw.newLine();
			bw.close();
		} catch (IOException e) {
			e.printStackTrace();
		} finally {
			try {
				if (br != null)
					br.close();
			} catch (IOException ex) {
				ex.printStackTrace();
			}
		}
	}
	public static void main(String[] args) {
		final long startTime = System.currentTimeMillis();
		 balloon x = new balloon();
		 int arrows = 0;
		 for(int i = 0;i<x.GetTests();i++){
			 arrows = x.pew(x.GetHeights(i), x.GetBalloonNum(i));
			 writeAnswer(arrows);
		 }
		 final long endTime = System.currentTimeMillis();

	}
}
