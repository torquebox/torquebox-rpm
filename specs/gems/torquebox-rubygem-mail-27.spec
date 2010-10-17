%global tree_prefix  torquebox-
%global ruby_sitelib /opt/jruby/lib/ruby/site_ruby/1.8
%global gem_dir      /opt/jruby/lib/ruby/gems/1.8
%global bin_dir      /opt/jruby/bin
%global gem_name     mail
%global gem_instdir  %{gem_dir}/gems/%{gem_name}-%{version}
%global ruby_abi     1.8-java

Name: torquebox-rubygem-mail-27
Version: 2.2.7
Release: 1%{?dist}
Group: Development/Languages
License: GPLv2+ or Ruby
BuildArch: noarch
Summary: Mail provides a nice Ruby DSL for making, sending and reading emails
URL: http://github.com/mikel/mail
Source0: http://rubygems.org/gems/mail-2.2.7.gem

Provides: %{tree_prefix}rubygem(%{gem_name}) = %{version}

Requires: ruby(abi) = %{ruby_abi}

Requires: %{tree_prefix}rubygem(activesupport) >= 2.3.6
Requires: %{tree_prefix}rubygem(mime-types) >= 0
Requires: %{tree_prefix}rubygem(treetop) >= 1.4.5

%description

A really Ruby Mail handler.

%prep

%build

%install

rm -rf %{buildroot}
install -m 755 -d %{buildroot}%{bin_dir}
install -m 755 -d %{buildroot}%{gem_dir}
install -m 755 -d %{buildroot}%{gem_dir}/gems/mail-2.2.7/lib
gem install --local --bindir %{buildroot}%{bin_dir} --install-dir %{buildroot}%{gem_dir} --force --ignore-dependencies --platform ruby %{SOURCE0}

%clean

rm -rf %{buildroot}

%files

%defattr(-, root, root, -)
%{bin_dir}/
%{gem_dir}/gems/mail-2.2.7/
%{gem_dir}/cache/mail-2.2.7.gem
%{gem_dir}/specifications/mail-2.2.7.gemspec
%doc %{gem_dir}/doc/mail-2.2.7

%changelog

