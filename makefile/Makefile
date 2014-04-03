# 引入其他的mk文件，前面的-号表示如果需要引入的文件不存在的话，
# 就跳过，不然会报错
-include a.mk
hello:
	@echo "hello $(name)"

tar1 tar2:
	@echo "$@"

.PHONY: clean, tar

tar: tar1 tar2

clean:
	@ls

cmd:
	ls -l xx
	pwd

subsystem:
	cd subdir && $(MAKE)
name="world"


define foo
	echo $(shell whoami)
endef

test:
	$(foo)

