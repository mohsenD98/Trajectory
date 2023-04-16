var HevoTrackingUtils = (function() {
  var locationChangeSubject = {
    observers: [],
    value: getCookie('country_code'),
    next: function(countryCode) {
      this.value = countryCode;
      this.observers.forEach(function(observer) {
        observer(countryCode);
      });
    },
    subscribe: function(observer) {
      this.observers.push(observer);
      observer(this.value);
      var self = this;
      return {
        unsubscribe: function() {
          var deleteIndex = self.observers.findIndex(observer);
          self.observers.splice(deleteIndex, 1);
        }
      }
    }
  };

  function consumeVisitId() {
    window.visitId = undefined;

    var visitIdRef = getVisitIdFromCookie();

    if (!visitIdRef) {
      visitIdRef = generateNewVisitId();
      setCookie('hevo_visit_id', visitIdRef, 3650, '');
      setCookie('cookie_domain_updated', true, 3650, '');
    }

    window.visitId = visitIdRef;
  }

  function generateNewVisitId() {
    let deprecatedLocalStorageRef = localStorage.getItem('hevo_visit_id');

    if (deprecatedLocalStorageRef) {
      return deprecatedLocalStorageRef;
    }

    return uuidv4();
  }

  function getVisitIdFromCookie() {
    // Backword compatibility to update cookie domain.
    var cookieDomainUpdated = getCookie('cookie_domain_updated');
    let visitIdRef = getCookie('hevo_visit_id');

    if (cookieDomainUpdated !== 'true' && visitIdRef) {
      deleteCookie('hevo_visit_id');
      setCookie('hevo_visit_id', visitIdRef, 3650, '');
      setCookie('cookie_domain_updated', true, 3650, '');
    }

    return visitIdRef;
  }

  function uuidv4() {
    return 'xxxxxxxx-xxxx-4xxx-yxxx-xxxxxxxxxxxx'.replace(/[xy]/g, function(c) {
      var r = Math.random() * 16 | 0, v = c == 'x' ? r : (r & 0x3 | 0x8);
      return v.toString(16);
    });
  }

  function setCookie(cname, cvalue, exdays, path, domain) {
    var d = new Date();
    d.setTime(d.getTime() + (exdays * 24 * 60 * 60 * 1000));
    var expires = ';expires=' + d.toUTCString();

    var domain = ';domain=' + (domain || getBaseDomain());

    var path = ';path=/' + path;

    if (domain.split('.').length <= 1) {
      document.cookie = cname + '=' + cvalue + expires + path;
    } else {
      document.cookie = cname + '=' + cvalue + domain + expires + path;
    }
  }

  function deleteCookie(cname) {
    document.cookie = cname + '=;expires=Thu, 01 Jan 1970 00:00:01 GMT;';
  }

  function getBaseDomain() {
    return 'hevodata.com';
    // return window.location.host.split('.').slice(-2).join('.');
  }

  function getCookie(cname) {
    var name = cname + '=';
    var ca = document.cookie.split(';');
    for(var i = 0; i < ca.length; i++) {
        var c = ca[i];
        while (c.charAt(0) == ' ') {
            c = c.substring(1);
        }
        if (c.indexOf(name) == 0) {
            return c.substring(name.length, c.length);
        }
    }
    return "";
  }

  function saveRefererInCookie() {
    setCookie('document_referer', document.referrer, 3650, '');
  }

  function sendVisitIdToThirdPartyTrackers() {
    consumeVisitId();

    var visitId = window.visitId;

    if (window['intercomSettings']) {
      window['intercomSettings'].visit_id = visitId;
    }

    if (typeof mixpanel !== 'undefined') {
      mixpanel.identify(visitId);
    }

    var _hsq = window._hsq = window._hsq || [];
    _hsq.push(["identify", {
      visit_id: visitId
    }]);

    if (typeof heap !== 'undefined') {
      heap.addUserProperties({ 'visit_id': visitId });
    }
  }

  function getHeapIdAndSaveInCookie() {
    var intervalId = setInterval(function() {
      if (heap && heap.userId) {
        setCookie('hevo_heap_id', heap.userId, 3650, '');
        clearInterval(intervalId);
      }
    }, 5000);
  }

  function registerPageVisit() {
    saveRefererInCookie();
    var xhr = new XMLHttpRequest();
    xhr.withCredentials = true;

    var requestUrl = 'https://hevodata.com/hevo-utility/check-connection';
    if (window.location.host !== 'try.hevodata.com'
        && window.location.host !== 'resources.hevodata.com'
        && window.location.host.match(/^([a-zA-Z\d-]+\.){0,}hevodata\.com$/)
      ) {
      requestUrl = '/hevo-utility/check-connection';
    }

    xhr.open('GET', requestUrl, true);
    xhr.send(null);
    return xhr;
  }

  return {
    setCookie: setCookie,
    getCookie: getCookie,
    deleteCookie: deleteCookie,
    consumeVisitId: consumeVisitId,
    sendVisitIdToThirdPartyTrackers: sendVisitIdToThirdPartyTrackers,
    getHeapIdAndSaveInCookie: getHeapIdAndSaveInCookie,
    registerPageVisit: registerPageVisit,
    locationChangeSubject: locationChangeSubject
  }
}());
