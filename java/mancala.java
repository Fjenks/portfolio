package comp_251_a5;

import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.File;
import java.io.FileNotFoundException;
import java.io.FileWriter;
import java.io.IOException;
import java.util.ArrayList;
import java.util.Scanner;

public class mancala {
	private int tests;       
	ArrayList<int[]> boards = new ArrayList<int[]>();    
	mancala(){
		try {
	        Scanner f = new Scanner(new File("testMancala.txt"));
	        String[] ln = f.nextLine().split("\\s+"); 
	        this.tests = Integer.parseInt(ln[0]);
	        int test_number = 0;
	        int[] current_board = new int[12];
	        
	        for(int i = 0;i<tests;i++) {
	        	String[] line = f.nextLine().split("\\s+");
	        	for(int j = 0;j<12;j++){
	        		current_board[j] = Integer.parseInt(line[j]);
	        	}
	        	boards.add(current_board.clone());
	        }
	        
	        for(int i = 0;i<tests;i++) {
	        	for(int j = 0;j<12;j++){
	        	}
	        }
	        
	        f.close();
	     
	    }
	    catch (FileNotFoundException e){
	        System.out.println("File not found!");
	        System.exit(1);
	    }
	}
	public int[] makeMove(int[] board_state,int[] move){
		if(board_state[move[0]]==1){
			board_state[move[0]]=0; board_state[move[1]] = 0; board_state[move[2]] = 1;
		}
		else{
			board_state[move[0]]=1; board_state[move[1]] = 0; board_state[move[2]] = 0;
		}
		return board_state;
	}
	public boolean moveCheck(int[] move){
		if(move[0]==1&&move[1]==1&&move[2]==0){
			return true;
		}
		else if(move[0]==0&&move[1]==1&&move[2]==1){
			return true;
		}
		else{
			return false;
		}
	}
	public int play(int[] board){
		int final_pebbles = 0;
		int min_pebbles = 0;
		ArrayList<int[] >possible_moves = new ArrayList<int[]>();
		int[] ABC = new int[3];
		for(int i = 0;i<12;i++){
			if(board[i]==1){
				min_pebbles++;
			}
		}
		for(int i = 1;i<11;i++){
			
			ABC[0] = board[i-1];ABC[1] = board[i];ABC[2] = board[i+1];
			if(moveCheck(ABC)){
				possible_moves.add(new int[] {i-1,i,i+1});
			}
		}
		for(int i = 0;i<possible_moves.size();i++){
			int[] current_board = board.clone();
			current_board = makeMove(current_board,possible_moves.get(i));
			for(int j = 0;j<12;j++){
        	}
			final_pebbles = play(current_board);
			if(final_pebbles<min_pebbles){
				min_pebbles = final_pebbles;
			}
		}
		
		
		return min_pebbles;
	}
	
	public static void writeAnswer(int line) {
		BufferedReader br = null;
		File file = new File("testMancala_solution.txt");

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
	public int[] GetBoards(int index) {
		return this.boards.get(index);
	}
	public int GetTests() {
		return this.tests;
	}
	public static void main(String[] args) {
		int game = 0;
		final long startTime = System.currentTimeMillis();
		 mancala x = new mancala();
		 for(int i = 0; i<x.GetTests();i++){
			 game = x.play(x.GetBoards(i));
			 x.writeAnswer(game);
		 }
		 final long endTime = System.currentTimeMillis();

	}
}
