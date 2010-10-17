%global tree_prefix  torquebox-
%global ruby_sitelib /opt/jruby/lib/ruby/site_ruby/1.8
%global gem_dir      /opt/jruby/lib/ruby/gems/1.8
%global bin_dir      /opt/jruby/bin
%global gem_name     rails
%global gem_instdir  %{gem_dir}/gems/%{gem_name}-%{version}
%global ruby_abi     1.8-java

Name: torquebox-rubygem-rails-28
Version: 2.3.8
Release: 1%{?dist}
Group: Development/Languages
License: GPLv2+ or Ruby
BuildArch: noarch
Summary: Web-application framework with template engine, control-flow layer, and ORM
URL: http://www.rubyonrails.org
Source0: http://rubygems.org/gems/rails-2.3.8.gem

Provides: %{tree_prefix}rubygem(%{gem_name}) = %{version}

Requires: ruby(abi) = %{ruby_abi}

Requires: %{tree_prefix}rubygem(rake) >= 0.8.3
Requires: %{tree_prefix}rubygem(activesupport) = 2.3.8
Requires: %{tree_prefix}rubygem(activerecord) = 2.3.8
Requires: %{tree_prefix}rubygem(actionpack) = 2.3.8
Requires: %{tree_prefix}rubygem(actionmailer) = 2.3.8
Requires: %{tree_prefix}rubygem(activeresource) = 2.3.8

%description

    Rails is a framework for building web-application using CGI, FCGI, mod_ruby, or WEBrick
    on top of either MySQL, PostgreSQL, SQLite, DB2, SQL Server, or Oracle with eRuby- or Builder-based templates.

%prep

%build

%install

rm -rf %{buildroot}
install -m 755 -d %{buildroot}%{bin_dir}
install -m 755 -d %{buildroot}%{gem_dir}
install -m 755 -d %{buildroot}%{gem_dir}/gems/rails-2.3.8/lib
gem install --local --bindir %{buildroot}%{bin_dir} --install-dir %{buildroot}%{gem_dir} --force --ignore-dependencies --platform ruby %{SOURCE0}

%clean

rm -rf %{buildroot}

%files

%defattr(-, root, root, -)
%{bin_dir}/
%{gem_dir}/gems/rails-2.3.8/
%{gem_dir}/cache/rails-2.3.8.gem
%{gem_dir}/specifications/rails-2.3.8.gemspec
%doc %{gem_dir}/doc/rails-2.3.8

%changelog

