//----------------------------- includes --------------------------------------
#include <iostream>
#include <stdexcept>
#include <ctime>
#include <sys/time.h>
#include <thread>
#include <glog/logging.h>


//----------------------------- namespace -------------------------------------
using namespace std;

//----------------------------- outside func ----------------------------------
int okcoin_curl_get(char* url, size_t times);
int test_api();

//----------------------------- loc func --------------------------------------
inline int init_logging(char* fileName)
{
	google::InitGoogleLogging(fileName);
	google::SetLogDestination(google::GLOG_INFO,"./log/arb_info_");
	google::SetLogDestination(google::GLOG_WARNING,"./log/arb_warning_");
	google::SetLogDestination(google::GLOG_ERROR,"./log/arb_err_");
	google::SetLogDestination(google::GLOG_FATAL,"./log/arb_fatal_");

	//FLAGS_logbufsecs = 0;
	FLAGS_max_log_size = 128;
}

//----------------------------- thread func -----------------------------------
void task_get_RPC_data()
{
	LOG(INFO)<< "RPC task begin" << endl;
	okcoin_curl_get("https://www.okcoin.cn/api/v1/ticker.do?symbol=btc_cny", 100);
}


//----------------------------- main func -----------------------------------
int main(int argc, char** argv)
{
	struct timeval t1,t2;
	gettimeofday(&t1, NULL);

	clock_t t;
	t = clock();
	//init google log
	test_api();
	init_logging(argv[0]);
	LOG(INFO)<<"xxxxxxxxxx"<<endl;
	//read configure files
	//connect to database - mysql ? redis
	//fork be daemon
	//init threads-
	//threads for get data all the time
	std::thread thread_get_RPC_data(task_get_RPC_data);
	//threads for call python scripts
	//thread for listening rpc and commands
	//wait threads
	thread_get_RPC_data.join();

	t = clock() - t;

	gettimeofday(&t2, NULL);

	std::cout<< (double)t/CLOCKS_PER_SEC << endl;
	std::cout<< (double)(t2.tv_sec - t1.tv_sec) << endl;

    return 0;
}
