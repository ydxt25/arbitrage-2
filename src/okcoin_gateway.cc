/*
 * =====================================================================================
 *
 *       Filename:  okcoin_gateway.cc
 *
 *    Description:  api for access okcoin json rpc
 *
 *        Version:  1.0
 *        Created:  02/17/2016 05:00:02 PM
 *       Revision:  none
 *       Compiler:  g++
 *
 *         Author:  chenhao
 *        Company:  
 *
 * =====================================================================================
 */

#include <iostream>
#include <fstream>
#include <memory>
#include <curl/curl.h>
#include <curl/easy.h>
#include <string.h>

size_t callback_get_data( void *ptr, size_t size, size_t nmemb, void *userp)
{
	//std::cout<<static_cast<char*>(ptr)<<std::endl;
	size_t nsize = size * nmemb;
	memcpy(userp, ptr, nsize);
	return nsize;
}

int okcoin_curl_get(char* url, size_t times)
{
	//output file
	auto of_del = [](std::ofstream* f){
		f->close();
		std::cout<<"output file closed\n";
		};
	std::shared_ptr<std::ofstream> myof(new std::ofstream, of_del);
	myof->open("okcoin_output.txt");

	//get begin
    CURL *curl;
	CURLcode res;
    curl = curl_easy_init();

	char buffer[10240] = "";

    curl_easy_setopt(curl, CURLOPT_URL, url);        
	curl_easy_setopt(curl, CURLOPT_WRITEFUNCTION, callback_get_data);
	curl_easy_setopt(curl, CURLOPT_WRITEDATA, buffer);

    if (curl != NULL)
    {
		while (times--){
			memset(buffer, 0x00, sizeof(buffer));
        	res = curl_easy_perform(curl);
			if(res != CURLE_OK)
			{
					continue;
			}
			(*myof)<<buffer<<'\n';
		}
        curl_easy_cleanup(curl);
    }
    return res;
}
