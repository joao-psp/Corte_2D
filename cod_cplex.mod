/*********************************************
 * OPL 12.8.0.0 Model
 * Author: joaop
 * Creation Date: 30/06/2018 at 18:20:09
 *********************************************/
int srectangles = 21;
range m = 1..srectangles;
int L0 = 24	;
int W0 = 24;

range L = 0..L0-1;
range W = 0..W0-1;

int l[m] = [8,3,8,3,3,3,2,9,2,8,8,3,3,7,9,5,2,3,4,5,2];
int w[m] = [4,7,2,4,3,2,1,3,3,1,5,1,6,1,2,4,6,5,4,3,2];
int v[m] = [66,35,24,17,11,8,2,24,21,10,2,25,18,26,10,9,8,7,6,5,4];

int Q[m] = [2,1,3,5,2,2,1,5,2,4,5,6,2,1,8,2,4,5,6,2,9];
int P[m] = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0];


//int l[m] = [8,3,8,3,3,3,2];
//int w[m] = [4,7,2,4,3,2,1];
//int v[m] = [66,35,24,17,11,8,2];
//
//int Q[m] = [2,1,3,5,2,2,1];
//int P[m] = [0,0,0,0,0,0,0];

int a[i in m][p in L][q in W][r in L][s in W];

execute calc_a{
for(var i in m)
	for(var p in L)
		for(var q in W)
			for(var r in L)
				for(var s in W)
					if(0<=p && p<=r && r <= ((p+l[i])-1) && ((p+l[i])-1)<= (L0-1) && 
						0<=q && q<=s && s<=((q+w[i])-1) && ((q+w[i])-1)<=(W0-1)){
						a[i][p][q][r][s] = 1;
					}else{
						a[i][p][q][r][s] = 0;	
					}

}

dvar boolean x[i in m][p in L][q in W];

maximize
  sum(i in m, p in L, q in W : 0<=p && p<=(L0-l[i]) && 0<=q && q<=(W0-w[i])) v[i]*x[i][p][q];
  
subject to{
	rest1:
	forall(r in L, s in W)
	  sum(i in m, p in L, q in W) a[i][p][q][r][s]*x[i][p][q] <=1;
	rest2:
	forall(i in m){
		sum(p in L, q in W) x[i][p][q] >= P[i];
		sum(p in L, q in W) x[i][p][q] <= Q[i];}
}
