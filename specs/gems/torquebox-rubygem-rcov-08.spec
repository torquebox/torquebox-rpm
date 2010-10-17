%global tree_prefix  torquebox-
%global ruby_sitelib /opt/jruby/lib/ruby/site_ruby/1.8
%global gem_dir      /opt/jruby/lib/ruby/gems/1.8
%global bin_dir      /opt/jruby/bin
%global gem_name     rcov
%global gem_instdir  %{gem_dir}/gems/%{gem_name}-%{version}
%global ruby_abi     1.8-java

Name: torquebox-rubygem-rcov-08
Version: 0.9.8
Release: 1%{?dist}
Group: Development/Languages
License: GPLv2+ or Ruby
BuildArch: noarch
Summary: Code coverage analysis tool for Ruby
URL: http://github.com/relevance/rcov
Source0: http://rubygems.org/gems/rcov-0.9.8-java.gem

Provides: %{tree_prefix}rubygem(%{gem_name}) = %{version}

Requires: ruby(abi) = %{ruby_abi}


%description

rcov is a code coverage tool for Ruby. It is commonly used for viewing overall test unit coverage of target code.  It features fast execution (20-300 times faster than previous tools), multiple analysis modes, XHTML and several kinds of text reports, easy automation with Rake via a RcovTask, fairly accurate coverage information through code linkage inference using simple heuristics, colorblind-friendliness...

%prep

%build

%install

rm -rf %{buildroot}
install -m 755 -d %{buildroot}%{bin_dir}
install -m 755 -d %{buildroot}%{gem_dir}
install -m 755 -d %{buildroot}%{gem_dir}/gems/rcov-0.9.8-java/lib
gem install --local --bindir %{buildroot}%{bin_dir} --install-dir %{buildroot}%{gem_dir} --force --ignore-dependencies --platform java %{SOURCE0}

%clean

rm -rf %{buildroot}

%files

%defattr(-, root, root, -)
%{bin_dir}/
%{gem_dir}/gems/rcov-0.9.8-java/
%{gem_dir}/cache/rcov-0.9.8-java.gem
%{gem_dir}/specifications/rcov-0.9.8-java.gemspec
%doc %{gem_dir}/doc/rcov-0.9.8-java

%changelog

