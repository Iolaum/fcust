FROM fedora:32

RUN dnf -y update
RUN dnf -y install python3-pip python3-tox make
RUN dnf clean all

ADD . /src

RUN useradd -ms /bin/bash user1
RUN useradd -ms /bin/bash user2
RUN groupadd common
RUN usermod -a -G common user1
RUN usermod -a -G common user2
RUN cd /src; pip install --upgrade pip; pip install .[dev]
