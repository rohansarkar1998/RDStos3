FROM centos
RUN dnf --disablerepo '*' --enablerepo=extras swap centos-linux-repos centos-stream-repos --assumeyes
RUN dnf distro-sync --assumeyes
RUN yum install python3 --assumeyes
RUN pip3 install pymysql
COPY Map.py /opt
WORKDIR /opt
RUN python3 Map.py
