.PHONY: purge
purge:
ifeq ($(TRAVIS_BRANCH),master)
	@curl -X POST --header "Fastly-Key: $(FASTLY_API_TOKEN)" https://api.fastly.com/service/$(FASTLY_SERVICE_ID)/purge_all
endif
