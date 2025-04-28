#include <gpiod.h>
#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <sys/time.h>
#include <stdbool.h>

int event_cb(int event, unsigned int offset, const struct timespec *timestamp, void *unused)
{
	if (event == GPIOD_CTXLESS_EVENT_CB_RISING_EDGE){
		fprintf(stdout, "%ld.%09ld\n", timestamp->tv_sec, timestamp->tv_nsec);
	}
	return GPIOD_CTXLESS_EVENT_CB_RET_OK;
}

static char output_path[512] = "/hom/tornado/tornado";
static char output_file[512] = "output.txt";

int main(int argc, char *argv[])
{
	int offset;

	if (argc != 3) {
		fprintf(stderr, "usage: %s <controler> <offset>\n", argv[0]);
		exit(EXIT_FAILURE);
	}
	if (sscanf(argv[2], "%d", &offset) != 1) {
		fprintf(stderr, "invalid offset: %s\n", argv[2]);
		exit(EXIT_FAILURE);
	}

	gpiod_ctxless_event_monitor(argv[1], GPIOD_CTXLESS_EVENT_BOTH_EDGES, 
	                         offset, 0, argv[0], NULL, NULL, event_cb, NULL);

	return EXIT_SUCCESS;
}

